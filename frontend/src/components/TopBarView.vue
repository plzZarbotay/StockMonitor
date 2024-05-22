<template>
  <div id="app">
    <nav>
      <div class="left-nav">
        <router-link to="/">Главная</router-link>
        <router-link to="/about">О нас</router-link>
        <router-link to="/table">Акции</router-link>
      </div>
      <div class="center-nav">
        <input type="text" placeholder="Поиск..." />
      </div>
      <div class="right-nav">
        <router-link v-if="isLoggedIn" to="/profile">
          <img
            src="./static/user-icon.png"
            alt="Пррфиль"
            class="profile-icon"
          />
        </router-link>
        <router-link v-else to="/auth/login">Вход</router-link>
      </div>
    </nav>
    <router-view />
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  computed: {
    ...mapGetters("auth", ["isLoggedIn"]),
  },
};
</script>

<style>
#app {
  text-decoration: none;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 15px 40px;
  background-color: rgb(26, 41, 73);
}

.left-nav,
.right-nav {
  text-decoration: none;
  display: flex;
  align-items: center;
}

.left-nav a,
.right-nav a {
  text-decoration: none;
  font-weight: bold;
  color: #7198c0;
  margin: 0 20px;
}

.left-nav a.router-link-exact-active,
.right-nav a.router-link-exact-active {
  color: #42b983;
}

.center-nav {
  position: absolute;
  left: 50%;
  text-decoration: solid;
  color: #42b983;
  transform: translateX(-50%);
}

.center-nav input {
  padding: 5px 15px;
  width: calc(3 * 200px); /* Увеличение ширины в 3 раза */
  font-size: 16px;
  border: 1px solid #42b983;
  border-radius: 4px;
  background-color: rgb(64, 81, 119);
  color: #42b983;
}

.right-nav {
  width: 30px;
  height: 30px;
  border-radius: 50%;
}

.profile-icon {
  width: 50px;
  margin: -15px -15px;
}
</style>
