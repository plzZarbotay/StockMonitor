<template>
  <div id="app">
    <nav
      :class="{
        top_bar_light: isLightTheme,
        top_bar_dark: !isLightTheme,
      }"
    >
      <div class="left-nav">
        <router-link to="/">Главная</router-link>
        <router-link to="/about">О нас</router-link>
        <router-link to="/table">Акции</router-link>
      </div>
      <div
        :class="{
          'center-nav-light': isLightTheme,
          'center-nav': !isLightTheme,
        }"
      >
        <input
          type="text"
          placeholder="Поиск..."
          v-model="query"
          @input="handleSearch"
        />
        <ul v-if="searchResults.length && query" class="search-results">
          <li
            v-for="result in searchResults"
            :key="result.id"
            @click="goToStockDetails(result.ticker)"
          >
            {{ result.name }}
          </li>
        </ul>
      </div>
      <div class="theme-toggle" @click="toggleTheme">
        <div
          :class="{
            'toggle-circle': true,
            light: isLightTheme,
            dark: !isLightTheme,
          }"
        ></div>
      </div>
      <div class="right-nav">
        <router-link v-if="isLoggedIn" to="/profile">
          <img
            src="./static/user-icon.png"
            alt="Профиль"
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
import { mapGetters, mapActions } from "vuex";

export default {
  data() {
    return {
      query: "",
    };
  },
  computed: {
    ...mapGetters(["isLightTheme"]),
    ...mapGetters("auth", ["isLoggedIn"]),
    ...mapGetters("search_stocks", ["searchResults"]),
  },
  methods: {
    ...mapActions(["toggleTheme"]),
    ...mapActions("search_stocks", ["fetchSearchResults"]),
    handleSearch() {
      if (this.query.length > 0) {
        this.fetchSearchResults(this.query);
      }
    },
    goToStockDetails(ticker) {
      this.$router.push({ name: "stock", params: { name: ticker } });
    },
    toggleTheme() {
      this.$store.dispatch("toggleTheme");
    },
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

.top_bar_light {
  background-color: #548f64;
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
  position: relative;
  text-decoration: solid;
  color: #42b983;
}

.center-nav-light {
  position: relative;
  text-decoration: solid;
  color: #42b983;
}

.center-nav-light input {
  padding: 5px 15px;
  width: 600px; /* Фиксированная ширина */
  font-size: 16px;
  border: 1px solid #42b983;
  border-radius: 4px;
  background-color: rgb(255, 255, 255);
  color: #42b983;
}

.center-nav input {
  padding: 5px 15px;
  width: 600px; /* Фиксированная ширина */
  font-size: 16px;
  border: 1px solid #42b983;
  border-radius: 4px;
  background-color: rgb(64, 81, 119);
  color: #42b983;
}

.search-results {
  font-size: medium;
  position: absolute;
  top: 40px; /* Расстояние от input до списка */
  left: 50%;
  transform: translateX(-50%);
  width: 600px; /* Совпадает с шириной input */
  background-color: rgb(80, 97, 134);
  border: 1px solid #42b983;
  border-radius: 4px;
  list-style: none;
  padding: 0;
  margin: 0;
  z-index: 1000;
  text-align: left;
}

.search-results li {
  padding: 10px;
  border-bottom: 1px solid #ddd;
  cursor: pointer;
}

.search-results li:hover {
  background-color: rgb(64, 81, 119);
}

.right-nav {
  display: flex;
  align-items: center;
}

.profile-icon {
  width: 50px;
  border-radius: 50%;
}

.theme-toggle {
  cursor: pointer;
  padding: 5px;
  display: flex;
  align-items: center;
}

.toggle-circle {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  transition: background-color 0.3s ease, box-shadow 0.3s ease;
}

.light {
  background-color: white;
}

.dark {
  background-color: black;
}

.theme-toggle:hover {
  transform: scale(1.1);
}
</style>
