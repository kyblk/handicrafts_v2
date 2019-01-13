<template>
    <div is="main">

        <!-- Меню получает значение "active" в качестве класса. -->

        <!-- Чтобы предотвратить "прыжки" страницы при изменении ссылки, используем модификатор "prevent" (сокращение для preventDefault). -->

        <nav v-bind:class="active" v-on:click.prevent>

            <!-- Когда происходит нажатие на ссылку, вызываем метод makeActive, определенный как js-сущность Vue. -->

            <a href="#" class="home" v-on:click="makeActive('home')">Главная</a>
            <a href="#" class="projects" v-on:click="makeActive('projects')">Проекты</a>
            <a href="#" class="services" v-on:click="makeActive('services')">Услуги</a>
            <a href="#" class="contact" v-on:click="makeActive('contact')">Контакты</a>
        </nav>

        <!-- Шаблонное значение будет заменено на значение переменной "active". Все изменения будут автоматически отражены на странице. -->

        <p>Выбран класс <b>{{active}}</b></p>
    </div>
</template>

<script>
    export default {
        data() {
            return {active: 'home'}

        },

        // Функции, которые будем использовать.
        methods: {
            makeActive: function (item) {
                // Когда модель будет изменена, представление обновится.
                this.active = item;
            }
        }
    }
</script>