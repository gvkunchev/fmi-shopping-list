window.onload = function(){
    var items = document.querySelectorAll('.list-item input');
    for (var i=0; i<items.length; i++){
        items[i].onchange = function(){
            if (this.checked){
                this.parentElement.classList.add("bought-item");
            }
            else{
                this.parentElement.classList.remove("bought-item");
            }
        }
        items[i].parentElement.onclick = function(){
            input = this.querySelector('input');
            input.checked = !input.checked;
            input.onchange();
        }
        items[i].onchange();
    }
}