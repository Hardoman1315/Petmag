// my_app/static/my_app/js/script.js
$(document).ready(function() {
    // Маска для телефонного номера
    $('#id_phone').mask('+7 (999) 999-99-99');

    // Валидация формы
    $('#contactForm').on('submit', function(event) {
        const name = $('#id_name').val();
        const phone = $('#id_phone').val();
        if (!name || !phone) {
            alert('Пожалуйста, заполните все поля.');
            event.preventDefault();
        }
    });

    // Функция для поиска контактов
    $('#search').on('input', function() {
        const query = $(this).val().toLowerCase();
        $('.contact').each(function() {
            const name = $(this).find('span:first').text().toLowerCase();
            $(this).toggle(name.includes(query));
        });
    });
});

function closeModal() {
    $('#modal').hide();
}

function deleteContact(id) {
    if (confirm('Вы уверены, что хотите удалить этот контакт?')) {
        $.ajax({
            url: `/delete_contact/${id}/`,
            type: 'POST',
            headers: {
                'X-CSRFToken': '{{ csrf_token }}'
            },
            success: function(response) {
                location.reload();
            },
            error: function() {
                alert('Произошла ошибка при удалении контакта.');
            }
        });
    }
}

function toggleFavorite(id) {
    $.ajax({
        url: `/toggle_favorite/${id}/`,
        type: 'POST',
        headers: {
            'X-CSRFToken': '{{ csrf_token }}'
        },
        success: function() {
            location.reload();
        },
        error: function() {
            alert('Произошла ошибка при изменении статуса избранного.');
        }
    });
}