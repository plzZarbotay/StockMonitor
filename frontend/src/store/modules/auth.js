// src/store/modules/auth.js
import axios from "axios";
import router from "../../router";

const state = {
  user: JSON.parse(localStorage.getItem("user")) || { email: "", password: "" },
  token: localStorage.getItem("token") || "",
  refreshToken: localStorage.getItem("refreshToken") || "",
  error: null,
  success: null,
};

const mutations = {
  SET_USER(state, user) {
    state.user = user;
  },
  SET_TOKEN(state, token) {
    state.token = token;
  },
  SET_REFRESH_TOKEN(state, refreshToken) {
    state.refreshToken = refreshToken;
  },
  SET_ERROR(state, error) {
    state.error = error;
  },
  SET_SUCCESS(state, success) {
    state.success = success;
  },
  LOGOUT(state) {
    state.user = { email: "", password: "" };
    state.token = "";
    state.refreshToken = "";
  },
};

const actions = {
  async register({ commit }, userData) {
    try {
      commit("SET_ERROR", null);
      commit("SET_SUCCESS", null);
      const response = await axios.post(
        "http://127.0.0.1:8000/api/v1/auth/register/",
        userData
      );

      const { access, refresh } = response.data;
      commit("SET_TOKEN", access);
      commit("SET_REFRESH_TOKEN", refresh);
      localStorage.setItem("token", access);
      localStorage.setItem("refreshToken", refresh);

      const user = { email: userData.email, password: userData.password };
      commit("SET_USER", user);
      localStorage.setItem("user", JSON.stringify(user));

      commit("SET_SUCCESS", "Registration successful");
      router.push("/");
    } catch (err) {
      commit("SET_ERROR", `An error occurred: ${err.message}`);
    }
  },
  async login({ commit }, credentials) {
    try {
      commit("SET_ERROR", null);
      commit("SET_SUCCESS", null);
      const response = await axios.post(
        "http://127.0.0.1:8000/api/v1/auth/",
        credentials
      );

      const { access, refresh } = response.data;
      commit("SET_TOKEN", access);
      commit("SET_REFRESH_TOKEN", refresh);
      localStorage.setItem("token", access);
      localStorage.setItem("refreshToken", refresh);

      const user = { email: credentials.email, password: credentials.password };
      commit("SET_USER", user);
      localStorage.setItem("user", JSON.stringify(user));

      commit("SET_SUCCESS", "Login successful");
      router.push("/");
    } catch (err) {
      commit("SET_ERROR", `An error occurred: ${err.message}`);
    }
  },
  logout({ commit }) {
    commit("LOGOUT");
    localStorage.removeItem("token");
    localStorage.removeItem("refreshToken");
    localStorage.removeItem("user");
    router.push("/auth/login");
  },
  async refreshToken({ commit, state }) {
    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/api/v1/auth/refresh-token/",
        {
          refresh: state.refreshToken,
        }
      );
      const { access } = response.data;
      commit("SET_TOKEN", access);
      localStorage.setItem("token", access);
    } catch (err) {
      commit("SET_ERROR", `An error occurred: ${err.message}`);
      commit("LOGOUT");
      localStorage.removeItem("token");
      localStorage.removeItem("refreshToken");
      localStorage.removeItem("user");
      router.push("/login");
    }
  },
};

const getters = {
  user: (state) => state.user,
  isLoggedIn: (state) => !!state.token,
  error: (state) => state.error,
  success: (state) => state.success,
};

export default {
  namespaced: true,
  state,
  mutations,
  actions,
  getters,
};
