/* =========================================================
   OKATENT — visor 3D de la carpa Cebú
   Estructura: frame.glb (modelo del fabricante).
   Techo, faldón, paredes y visera: geometría generada aquí,
   porque el modelo no trae el techo (roof.glb está roto).
   Requiere three r128 + GLTFLoader + DRACOLoader + OrbitControls.
   ========================================================= */
(function () {
  const CDN = 'https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/';
  const SIDES = ['front', 'right', 'back', 'left'];

  function srgb(hex) { return new THREE.Color(hex).convertSRGBToLinear(); }

  // La estructura se descarga y descomprime una sola vez aunque haya varios visores
  const modelCache = {};
  function loadModel(loader, url) {
    if (!modelCache[url]) modelCache[url] = new Promise((res, rej) => loader.load(url, res, undefined, rej));
    return modelCache[url];
  }

  function OkatentVisor(container, opts) {
    opts = Object.assign({
      model: 'frame.glb',
      span: 2.95,               // separación entre patas en metros (3×3)
      color: '#1B4A8C',
      walls: {},                // { back: 'lisa' | 'ventana' | 'puerta' | 'medio' }
      awning: false,
      autoRotate: true,
      camera: [5.5, 2.9, 6.5],
      target: [0, 1.25, 0],
      onReady: null
    }, opts || {});

    const api = { ready: null };
    if (!window.THREE || !THREE.GLTFLoader || !THREE.OrbitControls) {
      container.classList.add('visor-fallback');
      return api;
    }

    // ---------- escena ----------
    const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true, powerPreference: 'high-performance' });
    renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
    renderer.outputEncoding = THREE.sRGBEncoding;
    renderer.shadowMap.enabled = true;
    renderer.shadowMap.type = THREE.PCFSoftShadowMap;
    renderer.setClearColor(0x000000, 0);
    renderer.domElement.className = 'visor-canvas';
    container.appendChild(renderer.domElement);

    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(34, 1, 0.05, 200);
    camera.position.set(...opts.camera);

    if (THREE.RoomEnvironment) {
      const pmrem = new THREE.PMREMGenerator(renderer);
      scene.environment = pmrem.fromScene(new THREE.RoomEnvironment(), 0.04).texture;
    }
    scene.add(new THREE.HemisphereLight(0xffffff, 0xcfd6dc, THREE.RoomEnvironment ? 0.25 : 0.9));
    const sun = new THREE.DirectionalLight(0xffffff, THREE.RoomEnvironment ? 0.85 : 1.5);
    sun.position.set(5.5, 11, 6.5);
    sun.castShadow = true;
    sun.shadow.mapSize.set(2048, 2048);
    Object.assign(sun.shadow.camera, { left: -6, right: 6, top: 6, bottom: -6, near: 1, far: 30 });
    sun.shadow.bias = -0.0004;
    sun.shadow.radius = 5;
    scene.add(sun);

    const ground = new THREE.Mesh(new THREE.PlaneGeometry(40, 40), new THREE.ShadowMaterial({ opacity: 0.16 }));
    ground.rotation.x = -Math.PI / 2;
    ground.receiveShadow = true;
    scene.add(ground);

    const controls = new THREE.OrbitControls(camera, renderer.domElement);
    controls.target.set(...opts.target);
    controls.enableDamping = true;
    controls.dampingFactor = 0.07;
    controls.rotateSpeed = 0.7;
    controls.enablePan = false;
    controls.minDistance = 3.6;
    controls.maxDistance = 16;
    controls.minPolarAngle = 0.35;
    controls.maxPolarAngle = Math.PI / 2 - 0.04;
    controls.autoRotate = !!opts.autoRotate;
    controls.autoRotateSpeed = 0.9;
    controls.update();
    const stopAuto = () => { controls.autoRotate = false; };
    renderer.domElement.addEventListener('pointerdown', stopAuto);
    renderer.domElement.addEventListener('wheel', stopAuto, { passive: true });

    // ---------- materiales ----------
    const fabric = new THREE.MeshStandardMaterial({ color: srgb(opts.color), roughness: 0.9, metalness: 0, side: THREE.DoubleSide, envMapIntensity: 0.22 });
    const seam = new THREE.MeshStandardMaterial({ color: srgb(opts.color), roughness: 0.95, metalness: 0, envMapIntensity: 0.2 });
    const aluminium = new THREE.MeshStandardMaterial({ color: srgb('#D9DEE2'), roughness: 0.32, metalness: 0.75, envMapIntensity: 1 });
    const pvc = new THREE.MeshStandardMaterial({ color: srgb('#BFD0DA'), roughness: 0.1, metalness: 0, transparent: true, opacity: 0.35, side: THREE.DoubleSide, depthWrite: false, envMapIntensity: 1.2 });
    const darker = c => { const k = new THREE.Color(c); k.multiplyScalar(0.72); return k; };

    // ---------- medidas (se ajustan con el modelo) ----------
    const dims = { half: opts.span / 2, eave: 2.11, peak: 2.72, valance: 0.24 };
    const tent = new THREE.Group();
    scene.add(tent);
    const roofGroup = new THREE.Group();
    const wallsGroup = new THREE.Group();
    const awningGroup = new THREE.Group();
    tent.add(roofGroup, wallsGroup, awningGroup);

    function shadowAll(obj) { obj.traverse(o => { if (o.isMesh) { o.castShadow = true; o.receiveShadow = true; } }); }

    function buildRoof() {
      roofGroup.clear();
      const h = dims.half + 0.035, y = dims.eave, p = dims.peak;
      const v = [
        -h, y,  h,   h, y,  h,   0, p, 0,
         h, y,  h,   h, y, -h,   0, p, 0,
         h, y, -h,  -h, y, -h,   0, p, 0,
        -h, y, -h,  -h, y,  h,   0, p, 0,
      ];
      const g = new THREE.BufferGeometry();
      g.setAttribute('position', new THREE.Float32BufferAttribute(v, 3));
      g.computeVertexNormals();
      roofGroup.add(new THREE.Mesh(g, fabric));

      // costuras en las aristas del techo
      const corners = [[-h, h], [h, h], [h, -h], [-h, -h]];
      corners.forEach(([x, z]) => {
        const a = new THREE.Vector3(x, y, z), b = new THREE.Vector3(0, p, 0);
        const len = a.distanceTo(b);
        const s = new THREE.Mesh(new THREE.CylinderGeometry(0.012, 0.012, len, 6), seam);
        s.position.copy(a).lerp(b, 0.5);
        s.quaternion.setFromUnitVectors(new THREE.Vector3(0, 1, 0), b.clone().sub(a).normalize());
        roofGroup.add(s);
      });
      // remate superior
      const cap = new THREE.Mesh(new THREE.CylinderGeometry(0.05, 0.08, 0.06, 16), seam);
      cap.position.set(0, p + 0.01, 0);
      roofGroup.add(cap);

      // faldón
      const vh = dims.valance, w = h * 2 + 0.01;
      SIDES.forEach((side, i) => {
        const m = new THREE.Mesh(new THREE.BoxGeometry(w, vh, 0.012), fabric);
        m.position.set(0, y - vh / 2 + 0.005, h);
        const holder = new THREE.Group();
        holder.rotation.y = [0, Math.PI / 2, Math.PI, -Math.PI / 2][i];
        holder.add(m);
        roofGroup.add(holder);
      });
      // ribete del faldón
      SIDES.forEach((side, i) => {
        const m = new THREE.Mesh(new THREE.BoxGeometry(h * 2 + 0.02, 0.018, 0.016), seam);
        m.position.set(0, y - vh + 0.012, h + 0.001);
        const holder = new THREE.Group();
        holder.rotation.y = [0, Math.PI / 2, Math.PI, -Math.PI / 2][i];
        holder.add(m);
        roofGroup.add(holder);
      });
      shadowAll(roofGroup);
    }

    function wallMesh(type) {
      const w = dims.half * 2 - 0.02;
      const top = dims.eave - dims.valance * 0.4;
      const bottom = 0.03;
      const hgt = type === 'medio' ? 1.0 : top - bottom;
      const group = new THREE.Group();
      let hole = null;
      if (type === 'ventana') hole = { x: -0.55, y: 1.05, w: 1.1, h: 0.62 };
      if (type === 'puerta') hole = { x: -0.45, y: 0, w: 0.9, h: 1.9 };
      const shape = new THREE.Shape();
      if (hole && hole.y === 0) {
        // la puerta llega al suelo: el hueco forma parte del contorno
        shape.moveTo(-w / 2, 0); shape.lineTo(hole.x, 0); shape.lineTo(hole.x, hole.h); shape.lineTo(hole.x + hole.w, hole.h);
        shape.lineTo(hole.x + hole.w, 0); shape.lineTo(w / 2, 0); shape.lineTo(w / 2, hgt); shape.lineTo(-w / 2, hgt); shape.closePath();
      } else {
        shape.moveTo(-w / 2, 0); shape.lineTo(w / 2, 0); shape.lineTo(w / 2, hgt); shape.lineTo(-w / 2, hgt); shape.closePath();
        if (hole) {
          const hp = new THREE.Path();
          hp.moveTo(hole.x, hole.y); hp.lineTo(hole.x, hole.y + hole.h); hp.lineTo(hole.x + hole.w, hole.y + hole.h); hp.lineTo(hole.x + hole.w, hole.y); hp.closePath();
          shape.holes.push(hp);
          const pane = new THREE.Mesh(new THREE.PlaneGeometry(hole.w, hole.h), pvc);
          pane.position.set(hole.x + hole.w / 2, hole.y + hole.h / 2, 0);
          pane.renderOrder = 2;
          group.add(pane);
        }
      }
      if (hole) {
        const edge = new THREE.EdgesGeometry(new THREE.PlaneGeometry(hole.w, hole.h));
        const line = new THREE.LineSegments(edge, new THREE.LineBasicMaterial({ color: darker(fabric.color) }));
        line.position.set(hole.x + hole.w / 2, hole.y + hole.h / 2, 0.004);
        line.userData.edge = true;
        group.add(line);
      }
      const panel = new THREE.Mesh(new THREE.ShapeGeometry(shape), fabric);
      panel.castShadow = true; panel.receiveShadow = true;
      group.add(panel);
      group.position.y = bottom;
      return group;
    }

    let wallsState = {};
    function buildWalls() {
      wallsGroup.clear();
      SIDES.forEach((side, i) => {
        const type = wallsState[side];
        if (!type) return;
        const holder = new THREE.Group();
        holder.rotation.y = [0, Math.PI / 2, Math.PI, -Math.PI / 2][i];
        const wm = wallMesh(type);
        wm.position.z = dims.half + 0.025;
        holder.add(wm);
        wallsGroup.add(holder);
      });
    }

    let awningOn = !!opts.awning;
    function buildAwning() {
      awningGroup.clear();
      if (!awningOn) return;
      const w = dims.half * 2 + 0.07, depth = 0.95, drop = 0.34;
      const g = new THREE.PlaneGeometry(w, Math.hypot(depth, drop));
      const m = new THREE.Mesh(g, fabric);
      const ang = Math.atan2(drop, depth);
      m.rotation.x = -Math.PI / 2 + ang;
      m.position.set(0, dims.eave - dims.valance - drop / 2 + 0.02, dims.half + 0.04 + depth / 2);
      awningGroup.add(m);
      const val = new THREE.Mesh(new THREE.BoxGeometry(w, 0.16, 0.012), fabric);
      val.position.set(0, dims.eave - dims.valance - drop - 0.06, dims.half + 0.04 + depth);
      awningGroup.add(val);
      // tirantes de la visera
      [-1, 1].forEach(sx => {
        const a = new THREE.Vector3(sx * (dims.half + 0.01), dims.eave - 0.55, dims.half + 0.02);
        const b = new THREE.Vector3(sx * (dims.half + 0.02), dims.eave - dims.valance - drop, dims.half + 0.04 + depth);
        const len = a.distanceTo(b);
        const rod = new THREE.Mesh(new THREE.CylinderGeometry(0.014, 0.014, len, 8), aluminium);
        rod.position.copy(a).lerp(b, 0.5);
        rod.quaternion.setFromUnitVectors(new THREE.Vector3(0, 1, 0), b.clone().sub(a).normalize());
        awningGroup.add(rod);
      });
      shadowAll(awningGroup);
    }

    // ---------- carga de la estructura ----------
    const loader = new THREE.GLTFLoader();
    if (THREE.DRACOLoader) {
      const draco = new THREE.DRACOLoader();
      draco.setDecoderPath(CDN + 'libs/draco/');
      loader.setDRACOLoader(draco);
    }

    api.ready = new Promise(resolve => {
      loadModel(loader, opts.model).then(gltf => {
        const model = gltf.scene.clone(true);
        let legs = null, pole = null;
        model.traverse(o => {
          if (/Modelo.?CEBU/i.test(o.name)) legs = o;
          if (/mid.?arm/i.test(o.name)) pole = o;
        });
        const raw = new THREE.Box3().setFromObject(model);
        const legBox = legs ? new THREE.Box3().setFromObject(legs) : raw;
        const legSpan = legBox.max.x - legBox.min.x || 2.04;
        const k = opts.span / (legSpan - 0.04);
        const holder = new THREE.Group();
        holder.scale.set(k, 1, k);
        model.position.y = -raw.min.y;
        holder.add(model);
        tent.add(holder);

        dims.half = (legSpan * k) / 2;
        dims.eave = legBox.max.y - raw.min.y;
        if (pole) dims.peak = new THREE.Box3().setFromObject(pole).max.y - raw.min.y + 0.03;

        model.traverse(o => {
          if (!o.isMesh) return;
          let n = o, hide = false;
          while (n) { if (/canopy|awning|cloth|wall|door|window|curtain|Part2/i.test(n.name)) { hide = true; break; } n = n.parent; }
          if (hide) { o.visible = false; return; }
          o.material = aluminium;
          o.castShadow = true; o.receiveShadow = true;
        });

        buildRoof();
        wallsState = Object.assign({}, opts.walls);
        buildWalls();
        buildAwning();
        container.classList.add('visor-ready');
        if (opts.onReady) opts.onReady(api);
        resolve(api);
      }).catch(err => {
        console.error('Visor 3D:', err);
        container.classList.add('visor-fallback');
        resolve(api);
      });
    });

    // ---------- API ----------
    api.setColor = hex => {
      const c = srgb(hex);
      fabric.color.copy(c);
      seam.color.copy(c).multiplyScalar(0.8);
      wallsGroup.traverse(o => { if (o.userData.edge) o.material.color.copy(darker(fabric.color)); });
    };
    api.setWalls = obj => { wallsState = Object.assign({}, obj); buildWalls(); };
    api.setWall = (side, type) => { wallsState[side] = type || null; buildWalls(); };
    api.setAwning = on => { awningOn = !!on; buildAwning(); };
    api.resetView = () => { camera.position.set(...opts.camera); controls.target.set(...opts.target); controls.update(); };
    api.setAutoRotate = on => { controls.autoRotate = !!on; };
    seam.color.copy(fabric.color).multiplyScalar(0.8);

    // ---------- render ----------
    function resize() {
      const w = container.clientWidth, h = container.clientHeight;
      if (!w || !h) return;
      renderer.setSize(w, h, false);
      camera.aspect = w / h;
      camera.fov = w / h < 0.9 ? 44 : 34;
      camera.updateProjectionMatrix();
    }
    new ResizeObserver(resize).observe(container);
    resize();

    let visible = true;
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(e => { visible = e[0].isIntersecting; }).observe(container);
    }
    (function loop() {
      requestAnimationFrame(loop);
      if (!visible) return;
      controls.update();
      renderer.render(scene, camera);
    })();

    return api;
  }

  OkatentVisor.scripts = [
    CDN.replace('examples/js/', 'build/three.min.js'),
    CDN + 'loaders/GLTFLoader.js',
    CDN + 'loaders/DRACOLoader.js',
    CDN + 'controls/OrbitControls.js',
    CDN + 'environments/RoomEnvironment.js'
  ];

  window.OkatentVisor = OkatentVisor;
})();
