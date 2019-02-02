<template>
    <div is="main">
        <b-navbar toggleable="md" type="dark" variant="info">


            <b-navbar variant="faded" type="light">
                <b-navbar-brand href="#">
                    <img src="https://placekitten.com/g/30/30" class="d-inline-block align-top" alt="BV">
                    Katarina Fairy
                </b-navbar-brand>
            </b-navbar>

            <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>

            <b-collapse is-nav id="nav_collapse">

                <!-- Right aligned nav items -->
                <b-navbar-nav class="ml-auto">

                    <b-nav-item class="text-menu" href="#">Главная</b-nav-item>
                    <b-nav-item-dropdown>
                        <!-- Using button-content slot -->
                        <template slot="button-content">
                            <span class="text-menu">Каталог</span>
                        </template>
                        <b-dropdown-item href="#">Каталог</b-dropdown-item>
                        <b-dropdown-item href="#">Весь товар</b-dropdown-item>
                    </b-nav-item-dropdown>
                    <b-nav-item class="text-menu" href="#">О нас</b-nav-item>
                    <b-nav-item class="text-menu" href="#">Контакты</b-nav-item>
                </b-navbar-nav>


            </b-collapse>
        </b-navbar>
    </div>
</template>

<style scoped>
    .text-menu {
        font-weight: bold;
        font-size: 20px;
    }
</style>

<script>
    export default {}
</script>