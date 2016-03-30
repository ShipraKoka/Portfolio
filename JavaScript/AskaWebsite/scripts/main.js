$(document).ready(function () {
    var imageName = ["/content/images/afterfive edited small.jpg", "/content/images/active_edited_1.jpg"];
    var indexNum = 0;

    setInterval(function () {
        if (indexNum > 1) {
            indexNum = 0;
        }
        $("#change-design").fadeOut(300, function () {
            $("#change-design").attr("src", imageName[indexNum]);
            indexNum++;

            $("#change-design").fadeIn(500);
        })
    }, 2000);

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