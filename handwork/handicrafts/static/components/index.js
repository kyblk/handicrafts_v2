import Vue from 'vue';
import BootstrapVue from 'bootstrap-vue';

import MainSlider from './MainSlider.vue';
import CatalogList from './CatalogList.vue';
import ProductList from './ProductList.vue';


Vue.use(BootstrapVue);

Vue.prototype.$hostname = document.location.origin;
Vue.prototype.$hostname_api = document.location.origin + '/api';
Vue.prototype.$pathname = document.location.pathname;


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




