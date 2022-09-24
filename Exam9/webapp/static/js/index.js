async function sendLike(event) {
    event.preventDefault();
    let target = event.target;
    let url = target.href;
    let response = await fetch(url);
    if (response.status !== 202) {
        console.log('Ошибка')
        console.log(response)
    } else {
        if (target.innerText === "Добавить в избранное") {
            target.innerText = "Удалить из избранного";
            target.href = url.replace('add', 'remove');
        } else {
            target.innerText = "Добавить в избранное";
            target.href = url.replace('remove', 'add');
        }
    }
}

function onloadFunc() {

    let likes = document.getElementsByClassName("likes");
    for (let i = 0; i < likes.length; i++) {
        likes[i].addEventListener("click", sendLike);
    }
}
window.addEventListener("load", onloadFunc)
