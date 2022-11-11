window.onload = function(){
    var items = document.querySelectorAll('.list-item input');
    for (var i=0; i<items.length; i++){
        // Change class of the item on bought status change
        items[i].onchange = function(){
            if (this.checked){
                this.parentElement.classList.add("bought-item");
            }
            else{
                this.parentElement.classList.remove("bought-item");
            }
        }
        // Change bought status on click
        items[i].parentElement.onclick = function(){
            input = this.querySelector('input');
            state = input.checked ? 0 : 1;
            fetch('/toggle_item?id=' + input.dataset.id + '&state=' + state).then(function (response) {
                if (response.ok) {return response.json();}
                return Promise.reject(response);
            }).then(function (data) {
                input.checked = data['state'];
                input.onchange();
            }).catch(function (err) {
                console.warn('Unable to toggle the item state.', err);
            });
        }
        // Trigger initial class allocation
        items[i].onchange();
        // Remove element on x-button click
        var remove_button = items[i].parentElement.querySelector('.remove-item');
        remove_button.onclick = function(event){
            var row = this.parentElement;
            var input = row.querySelector('input');
            fetch('/remove_item?id=' + input.dataset.id).then(function (response) {
                if (response.ok) {return response.json();}
                return Promise.reject(response);
            }).then(function (data) {
                row.remove();
            }).catch(function (err) {
                console.warn('Unable to toggle the item state.', err);
            });
            event.stopPropagation();
        }
    }
}



