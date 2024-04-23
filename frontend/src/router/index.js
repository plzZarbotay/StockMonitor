import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import TableView from "../views/TableView.vue";
import ToolDescView from "@/views/ToolDescView.vue";
import ProfileView from "@/views/ProfileView.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/table",
    name: "table",
    component: TableView,
    // разделение кода на уровне маршрута
    // это генерирует отдельный чанк (about.[hash].js) для этого маршрута
    // который загружается лениво при посещении маршрута.
  },
  {
    path: "/description",
    name: "description",
    component: ToolDescView,
  },
  {
    path: "/profile",
    name: "profile",
    component: ProfileView,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
