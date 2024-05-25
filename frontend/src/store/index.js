import { createStore } from "vuex";
//import axios from "axios";
import auth from "./modules/auth";
import selected_chart from "./modules/selected_chart";
import search_stocks from "./modules/search_stocks";
import all_stocks_table from "./modules/all_stocks_table";

export default createStore({
  state: {
    theme: "dark", // по умолчанию используется светлая тема
  },
  mutations: {
    toggleTheme(state) {
      state.theme = state.theme === "light" ? "dark" : "light";
    },
  },
  actions: {
    toggleTheme({ commit }) {
      commit("toggleTheme");
    },
  },
  getters: {
    isLightTheme(state) {
      return state.theme === "light";
    },
    isDarkTheme(state) {
      return state.theme === "dark";
    },
  },
  modules: {
    auth,
    selected_chart,
    search_stocks,
    all_stocks_table,
  },
});
