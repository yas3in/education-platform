document.addEventListener('DOMContentLoaded', () => {
    const year = document.getElementById('year');
    if (year) year.textContent = new Date().getFullYear();

    const flipCard = document.getElementById('authFlipCard');
    if (!flipCard) return;

    const setAuthMode = (mode, pushUrl = true) => {
        if (mode === 'login') {
            flipCard.classList.add('is-flipped');
        } else {
            flipCard.classList.remove('is-flipped');
        }
        if (pushUrl && window.history && window.history.replaceState) {
            const url = new URL(window.location.href);
            url.searchParams.set('mode', mode);
            window.history.replaceState({}, '', url);
        }
    };

    // Flip buttons inside the card ("ورود" / "ثبت نام")
    document.querySelectorAll('[data-flip-to]').forEach((btn) => {
        btn.addEventListener('click', () => {
            setAuthMode(btn.getAttribute('data-flip-to'));
        });
    });

    // Navbar "ورود" / "ثبت نام" buttons when already on the auth page
    document.querySelectorAll('[data-auth-mode]').forEach((link) => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            setAuthMode(link.getAttribute('data-auth-mode'));
        });
    });
});
