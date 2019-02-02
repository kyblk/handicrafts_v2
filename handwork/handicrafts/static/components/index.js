import Vue from 'vue';
import BootstrapVue from 'bootstrap-vue';

import NavbarMenu from './NavbarMenu.vue';
import MainSlider from './MainSlider.vue';
import CatalogList from './CatalogList.vue';
import ProductList from './ProductList.vue';


Vue.use(BootstrapVue);

new Vue({
  el: '#navbar-menu-component',
  render: h => h(NavbarMenu)
});

new Vue({
  el: '#main-slider-component',
  render: h => h(MainSlider)
});

new Vue({
  el: '#catalog-list-component',
  render: h => h(CatalogList)
});

new Vue({
  el: '#product-list-component',
  render: h => h(ProductList)
});




