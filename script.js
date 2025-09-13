
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({ alpha: true });
renderer.setSize(window.innerWidth, window.innerHeight);
document.getElementById('background-tooth').appendChild(renderer.domElement);

const geometry = new THREE.TorusKnotGeometry(10, 3, 100, 16);
const material = new THREE.MeshBasicMaterial({ color: 0xffffff, transparent: true, opacity: 0.5 });
const tooth = new THREE.Mesh(geometry, material);
scene.add(tooth);

camera.position.z = 30;

function animate() {
    requestAnimationFrame(animate);
    tooth.rotation.x += 0.01;
    tooth.rotation.y += 0.01;
    renderer.render(scene, camera);
}
animate();

window.addEventListener('resize', () => {
    renderer.setSize(window.innerWidth, window.innerHeight);
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
});


const sections = document.querySelectorAll('.section');
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        entry.target.classList.toggle('in-view', entry.isIntersecting);
      
        if (entry.isIntersecting) {
            const scrollPosition = window.scrollY;
            tooth.position.y = -scrollPosition * 0.001;
            document.getElementById('background-tooth').style.transform = `translate(-50%, -50%) scale(${1 + scrollPosition * 0.0001})`;
        }
    });
}, { threshold: 0.1 });

sections.forEach(section => observer.observe(section));


document.querySelectorAll('.navbar a').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const targetId = this.getAttribute('href').substring(1);
        document.getElementById(targetId).scrollIntoView({ behavior: 'smooth' });
    });
});

function openModal() { document.getElementById('appointmentModal').style.display = 'flex'; }
function closeModal() { document.getElementById('appointmentModal').style.display = 'none'; }

window.onclick = function(event) {
    const modal = document.getElementById('appointmentModal');
    if (event.target == modal) closeModal();
};

document.getElementById('appointmentForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const formData = new FormData(this);
    const data = { name: formData.get('name'), phone: formData.get('phone'), comment: formData.get('comment') };
    console.log('Отправленные данные:', data);
    alert('Заявка отправлена! Доктор Жавлонбек свяжется с вами.');
    closeModal();
    this.reset();
});
