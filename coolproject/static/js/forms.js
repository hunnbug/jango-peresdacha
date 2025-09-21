document.addEventListener('DOMContentLoaded', function() {
    initFormEnhancements();
    initDatePickers();
    initFileUploads();
    initFormValidation();
});

function initFormEnhancements() {
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        const firstField = form.querySelector('input:not([type="hidden"]), select, textarea');
        if (firstField) {
            firstField.focus();
        }
        
        form.addEventListener('submit', function(e) {
            if (!validateForm(this)) {
                e.preventDefault();
                showFormErrors(this);
            }
        });
    });
}

function initDatePickers() {
    const dateInputs = document.querySelectorAll('input[type="date"]');
    dateInputs.forEach(input => {
        if (input.name.includes('date_of_birth') || input.name.includes('birth')) {
            input.max = new Date().toISOString().split('T')[0];
        }
        
        if (input.name.includes('due_date') || input.name.includes('future')) {
            input.min = new Date().toISOString().split('T')[0];
        }
        
        input.addEventListener('focus', function() {
            this.style.borderColor = '#0d6efd';
            this.style.boxShadow = '0 0 0 0.25rem rgba(13, 110, 253, 0.15)';
        });
        
        input.addEventListener('blur', function() {
            this.style.borderColor = '';
            this.style.boxShadow = '';
        });
    });
}

function initFileUploads() {
    const fileInputs = document.querySelectorAll('input[type="file"]');
    fileInputs.forEach(input => {
        input.addEventListener('change', function() {
            const file = this.files[0];
            if (file) {
                // Проверяем размер файла (максимум 5MB)
                if (file.size > 5 * 1024 * 1024) {
                    alert('Размер файла не должен превышать 5MB');
                    this.value = '';
                    return;
                }
                
                if (this.accept.includes('image')) {
                    if (!file.type.startsWith('image/')) {
                        alert('Пожалуйста, выберите изображение');
                        this.value = '';
                        return;
                    }
                    
                    showImagePreview(this, file);
                }
            }
        });
    });
}

function showImagePreview(input, file) {
    const reader = new FileReader();
    reader.onload = function(e) {
        const existingPreview = input.parentNode.querySelector('.image-preview');
        if (existingPreview) {
            existingPreview.remove();
        }
        
        const preview = document.createElement('div');
        preview.className = 'image-preview mt-2';
        preview.innerHTML = `
            <img src="${e.target.result}" class="img-thumbnail" style="max-width: 200px; max-height: 200px;">
            <div class="text-muted small mt-1">Превью: ${file.name}</div>
        `;
        
        input.parentNode.appendChild(preview);
    };
    reader.readAsDataURL(file);
}

function initFormValidation() {
    const inputs = document.querySelectorAll('input, select, textarea');
    inputs.forEach(input => {
        input.addEventListener('blur', function() {
            validateField(this);
        });
        
        input.addEventListener('input', function() {
            clearFieldError(this);
        });
    });
}

function validateField(field) {
    const value = field.value.trim();
    const fieldType = field.type;
    const fieldName = field.name;
    const isRequired = field.hasAttribute('required');
    
    clearFieldError(field);
    
    if (isRequired && !value) {
        showFieldError(field, 'Это поле обязательно для заполнения');
        return false;
    }
    
    if (fieldType === 'email' && value) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(value)) {
            showFieldError(field, 'Введите корректный email адрес');
            return false;
        }
    }
    
    if ((fieldType === 'tel' || fieldName.includes('phone')) && value) {
        const phoneRegex = /^[\+]?[0-9\s\-\(\)]{10,}$/;
        if (!phoneRegex.test(value)) {
            showFieldError(field, 'Введите корректный номер телефона');
            return false;
        }
    }
    
    if (fieldName.includes('_id') && value) {
        const idRegex = /^[A-Za-z0-9]+$/;
        if (!idRegex.test(value)) {
            showFieldError(field, 'ID может содержать только буквы и цифры');
            return false;
        }
    }
    
    if (fieldName.includes('grade') && value) {
        const grade = parseFloat(value);
        if (isNaN(grade) || grade < 1 || grade > 5) {
            showFieldError(field, 'Оценка должна быть от 1 до 5');
            return false;
        }
    }
    
    return true;
}

function validateForm(form) {
    let isValid = true;
    const inputs = form.querySelectorAll('input, select, textarea');
    
    inputs.forEach(input => {
        if (!validateField(input)) {
            isValid = false;
        }
    });
    
    return isValid;
}

function showFieldError(field, message) {
    field.classList.add('is-invalid');
    
    let errorDiv = field.parentNode.querySelector('.invalid-feedback');
    if (!errorDiv) {
        errorDiv = document.createElement('div');
        errorDiv.className = 'invalid-feedback';
        field.parentNode.appendChild(errorDiv);
    }
    
    errorDiv.textContent = message;
    errorDiv.style.display = 'block';
}

// Очистить ошибку поля
function clearFieldError(field) {
    field.classList.remove('is-invalid');
    const errorDiv = field.parentNode.querySelector('.invalid-feedback');
    if (errorDiv) {
        errorDiv.style.display = 'none';
    }
}

// Показать ошибки формы
function showFormErrors(form) {
    const firstError = form.querySelector('.is-invalid');
    if (firstError) {
        firstError.scrollIntoView({ behavior: 'smooth', block: 'center' });
        firstError.focus();
    }
}

// Автозаполнение связанных полей
function initRelatedFields() {
    // Пример: при выборе класса автоматически фильтровать учеников
    const classSelect = document.querySelector('select[name="class_group"]');
    const studentSelect = document.querySelector('select[name="student"]');
    
    if (classSelect && studentSelect) {
        classSelect.addEventListener('change', function() {
            const selectedClass = this.value;
            const options = studentSelect.querySelectorAll('option');
            
            options.forEach(option => {
                if (option.value === '' || option.dataset.class === selectedClass) {
                    option.style.display = '';
                } else {
                    option.style.display = 'none';
                }
            });
        });
    }
}

// Инициализация связанных полей
initRelatedFields();
