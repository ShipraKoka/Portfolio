﻿$(document).ready(function () {

    // Swap Images------------------------
    var imageName = ["/content/images/active_edited_1.jpg", "/content/images/evening edited 1.jpg", "/content/images/afterfive edited small.jpg"];
    var indexNum = 0;

    setInterval(function () {
        if (indexNum > 2) {
            indexNum = 0;
        }
        $(".image-swap").fadeOut(300, function () {
            $(".image-swap").attr("src", imageName[indexNum]);
            indexNum++;

            $(".image-swap").fadeIn(500);
        })
    }, 5000);

    // Smooth Scroll-----------------------
    $(function () {
        $('a[href*="#"]:not([href="#"])').click(function () {
            if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
                var target = $(this.hash);
                target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
                if (target.length) {
                    $('html, body').animate({
                        scrollTop: target.offset().top
                    }, 1000);
                    return false;
                }
            }
        });
    });
});