//星を作る関数。n は星の個数。多いほど星が多く振ります。
function starMaker(n) {
    var star = document.createElement("div");
    star.className = "star";
    star.textContent = "★";
    for(var i = 0; i < n; i++) {
        starSet(star);
    }
}

//星のセッティングをする関数。
function starSet(clone) {
    var starClone = clone.cloneNode(true);
    var starStyle = starClone.style;

    //星の位置（left）、アニメーションの遅延時間（animation-delay）、サイズ（font-size）をランダムで指定
    starStyle.left = 100 * Math.random() + "%";
    starStyle.animationDelay = 20 * Math.random() + "s";
    starStyle.fontSize = ~~(50 * Math.random() + 5) + "px";
    document.body.appendChild(starClone);

    //星一つのアニメーションが終わったら新しい星を生成
    starClone.addEventListener("animationend", function() {
        this.parentNode.removeChild(this);
        var star = document.createElement("div");
        star.className = "star";
        star.textContent = "★";
        starSet(star);
    }, false)
}

//使用例。星を50個ふらせます。
starMaker(30)

/*ローディング終わりの拾得*/
window.onload = function() {
    const spinner = document.getElementById('loading');
    spinner.classList.add('loaded');
 }
