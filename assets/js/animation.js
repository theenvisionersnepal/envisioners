var tl = gsap.timeline();
gsap.registerPlugin(ScrollTrigger);

tl.from(".content li", 1, {
    scrollTrigger: {
        trigger: '.showcase',
        start: 'top center',
    },
    scale: 1.2,
    y: -100,
    opacity: 1,
    delay: 0.5,
    pinSpacing: false,
    stagger: {
        amount: 2,

    }
});
var introgsap = gsap.timeline()
introgsap.from(".introduction .intro-info p", 1.5, {
    scrollTrigger: {
        trigger: '.introduction',
        start: 'top center',
    },
    ease: "bounce.out",
    opacity: 0,
    x: -100,
});
introgsap.from(".introduction .intro-info h1", 1, {
    scrollTrigger: {
        trigger: '.introduction',
        start: 'top center',
    },
    opacity: 0,
    x: 100,
});
introgsap.from("#knowmore", 0.5, {
    scrollTrigger: {
        trigger: '.introduction',
        start: 'top center',
    },
    opacity: 0,
    y: 50,
});
gsap.to('#knowmore', 0.5, {
    scrollTrigger: {
        trigger: '#knowmore',
        start: 'bottom bottom',
    },
    background: "#005dff",
});

gsap.to('.blogs', 1, {
    scrollTrigger: {
        trigger: '.blogs',
        start: 'top center',
    },
    background: "#005dff",
});

gsap.to('.social-feeds', 1, {
    scrollTrigger: {
        trigger: '.social-feeds',
        start: 'top center',
    },
    background: "#005dff",
});
gsap.to('.more-videos', 1, {
    scrollTrigger: {
        trigger: '.more-videos',
        start: 'top center',
    },
    background: "#005dff",
});
gsap.to(".introduction .intro-info p", 1, {
    scrollTrigger: {
        trigger: '.introduction',
        start: 'top center',
        scrub: true,
    },
    x: 100,
    y: -50,

});