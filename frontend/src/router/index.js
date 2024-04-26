import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import ToolDescView from "../components/ToolDescView.vue";
import ProfileView from "../views/ProfileView.vue";
import AboutView from "../views/AboutView.vue";
import TableView from "../views/TableView.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/profile",
    name: "profile",
    component: ProfileView,
  },
  {
    path: "/about",
    name: "about",
    component: AboutView,
  },
  {
    path: "/table",
    name: "table",
    component: TableView,
  },
  {
    path: "/stock/:name",
    name: "stock",
    component: ToolDescView,
    props: (route) => ({
      name: route.params.name,
      price: route.params.price,
      description: route.params.description,
    }),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
