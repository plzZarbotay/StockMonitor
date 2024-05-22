import axios from "axios";
import VueAxios from "vue-axios";
import VueApexCharts from "vue3-apexcharts";
import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

createApp(App)
  .use(store)
  .use(router)
  .use(VueAxios, axios)
  .use(VueApexCharts)
  .mount("#app");

App.config.globalProperties.$axios = axios;
