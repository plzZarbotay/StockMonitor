import router from "../../router";

const actions = {
  redirectAfterLogin() {
    router.push("/");
  },
  redirectAfterLogout() {
    router.push("/login");
  },
  setLocalStorage({ commit }, { key, value }) {
    localStorage.setItem(key, value);
    commit("SET_USER", JSON.parse(value));
  },
  removeLocalStorage({ commit }, key) {
    localStorage.removeItem(key);
    commit("LOGOUT");
  },
};

export default {
  namespaced: true,
  actions,
};
