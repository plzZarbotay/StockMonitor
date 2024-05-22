import { createRouter, createWebHistory } from "vue-router";
import store from "../store";
import HomeView from "../views/HomeView.vue";
import TableView from "../views/TableView.vue";
import ToolDescView from "../components/ToolDescView.vue";
import ProfileView from "../views/ProfileView.vue";
import AboutView from "../views/AboutView.vue";
import RegistrationView from "../views/RegistrationView.vue";
import LoginView from "../views/LoginView.vue";
import LogoutView from "../views/LogoutView.vue";
import AuthErrorView from "../views/AuthErrorView.vue";
import NotFoundView from "../views/NotFoundView.vue";
import ResetPasswordView from "../views/PasswordResetView.vue";

// Удалить позже
import TestView from "../components/ChartView.vue";

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
    path: "/stock/:name/",
    name: "stock",
    props: true,
    component: ToolDescView,
  },
  {
    path: "/auth/register",
    name: "registration",
    component: RegistrationView,
    meta: { requiresGuest: true },
  },
  {
    path: "/auth/login",
    name: "login",
    component: LoginView,
    meta: { requiresGuest: true },
  },
  {
    path: "/auth/logout",
    name: "LogoutView",
    component: LogoutView,
  },
  {
    path: "/auth/error",
    name: "AuthErrorView",
    component: AuthErrorView,
  },
  {
    path: "/:pathMatch(.*)*",
    name: "NotFoundView",
    component: NotFoundView,
  },
  {
    path: "/auth/password-reset",
    name: "ResetPasswordView",
    component: ResetPasswordView,
  },
  // Удалить позже
  {
    path: "/test-view",
    name: "TestView",
    component: TestView,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.requiresGuest)) {
    if (store.getters["auth/isLoggedIn"]) {
      next({ path: "/auth/error" });
    } else {
      next();
    }
  } else {
    next();
  }
});

export default router;
