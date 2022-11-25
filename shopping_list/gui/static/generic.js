$(document).ready(function(){

    // Handle removing of a shopping list
    $('.remove-list').bind('click', function(event){
        var row = $(this).parents('.list-group-item');
        var container = row.parents('.list-group');
        var id = $(this).data('id');
        var payload = {'csrfmiddlewaretoken': $('[name=csrfmiddlewaretoken]').val(),
                       'id': id};
        $.post("/remove_list", payload, function(data){
            if (data['state'] == 'removed'){
                $(row).remove();
                if(container.find('.list-group-item').length === 1){
                    $('.empty-list').removeClass('invisible');
                }
                else{
                    $('.empty-list').addClass('invisible');
                }
            }
        });
        event.stopPropagation();
        event.preventDefault();
    })

    // Handle buying a product
    $('.shopping-items .list-item').bind('click', function(){
        var input = $(this).find('input[type=checkbox]');
        var state = input.attr('checked') ? 0 : 1;
        var id = input.data('id');
        var payload = {'csrfmiddlewaretoken': $('[name=csrfmiddlewaretoken]').val(),
                       'id': id,
                       'state': state};
        $.post("/toggle_item", payload, function(data){
            if (data['state'] === true){
                input.attr('checked', 'checked').change();
            }
            else if (data['state'] === false){
                input.attr('checked', false).change();
            }
        });
    })
    $('input[type=checkbox').bind('change', function(){
        var button = $(this).parents('.list-item > .btn');
        if ($(this).attr('checked')){
            button.addClass('btn-success');
            button.removeClass('btn-secondary');
        }
        else{
            button.removeClass('btn-success');
            button.addClass('btn-secondary');
        }
    }).change();

    // Handle removing a product from shopping list
    $('.remove-item').bind('click', function(event){
        var row = $(this).parents('.list-group-item');
        var container = row.parents('.list-group');
        var id = $(this).data('id');
        var payload = {'csrfmiddlewaretoken': $('[name=csrfmiddlewaretoken]').val(),
                       'id': id};
        $.post("/remove_item", payload, function(data){
            if (data['state'] == 'removed'){
                $(row).remove();
                if(container.find('.list-group-item').length === 1){
                    $('.empty-list').removeClass('invisible');
                }
                else{
                    $('.empty-list').addClass('invisible');
                }
            }
        });
        event.stopPropagation();
        event.preventDefault();
    })
});