// src/axios.js
import axios from "axios";
import store from "./store";
import router from "./router";

const instance = axios.create({
  baseURL: "http://127.0.0.1:8000/api/v1/",
});

instance.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;

    if (error.response.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;
      try {
        await store.dispatch("auth/refreshToken");
        originalRequest.headers["Authorization"] =
          "Bearer " + store.state.auth.token;
        return instance(originalRequest);
      } catch (err) {
        store.dispatch("auth/logout");
        router.push("/login");
        return Promise.reject(err);
      }
    }
    return Promise.reject(error);
  }
);

export default instance;
