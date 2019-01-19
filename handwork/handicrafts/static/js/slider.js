import Vue from 'vue'
import BootstrapVue from 'bootstrap-vue'
import App from '../components/Slider.vue'

Vue.use(BootstrapVue);


new Vue({
  el: '#app',
  render: h => h(App)
})
