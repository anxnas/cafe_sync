// Функция для форматирования цены
function formatPrice(price) {
    return parseFloat(price).toFixed(2) + ' ₽';
}

// Функция для расчета общей стоимости заказа
function calculateTotal() {
    try {
        const itemsTextarea = document.getElementById('id_items_text');
        if (!itemsTextarea) return;

        const items = JSON.parse(itemsTextarea.value);
        let total = 0;

        for (const item of items) {
            if (item.price) {
                total += parseFloat(item.price);
            }
        }

        const totalElement = document.getElementById('calculated_total');
        if (totalElement) {
            totalElement.textContent = formatPrice(total);
        }
    } catch (error) {
        console.error('Ошибка при расчете общей стоимости:', error);
    }
}

// Инициализация при загрузке страницы
document.addEventListener('DOMContentLoaded', function() {
    // Добавляем классы Bootstrap к формам
    const formControls = document.querySelectorAll('input, select, textarea');
    formControls.forEach(element => {
        if (element.tagName === 'SELECT') {
            element.classList.add('form-select');
        } else {
            element.classList.add('form-control');
        }
    });

    // Инициализируем расчет общей стоимости
    const itemsTextarea = document.getElementById('id_items_text');
    if (itemsTextarea) {
        itemsTextarea.addEventListener('input', calculateTotal);
        calculateTotal(); // Рассчитываем при загрузке
    }
});