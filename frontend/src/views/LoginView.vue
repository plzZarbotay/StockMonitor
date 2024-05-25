<!-- components/Login.vue -->
<template>
  <div class="login-container">
    <h2>Вход</h2>
    <form @submit.prevent="loginUser">
      <div class="input-box">
        <input
          type="email"
          v-model="email"
          placeholder="Введите ваш email"
          required
        />
      </div>
      <div class="input-box">
        <input
          type="password"
          v-model="password"
          placeholder="Введите ваш пароль"
          required
        />
      </div>
      <div class="input-box button">
        <input type="submit" value="Войти" />
      </div>
      <div v-if="error" class="error">{{ error }}</div>
      <div v-if="success" class="success">{{ success }}</div>
    </form>
    <p class="">
      Нет аккаунта? ->
      <router-link to="/auth/register" class="register-link"
        >Регистрация</router-link
      >
    </p>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";

export default {
  data() {
    return {
      email: "",
      password: "",
    };
  },
  computed: {
    ...mapState("auth", ["error", "success"]),
  },
  methods: {
    ...mapActions("auth", ["login"]),
    loginUser() {
      this.login({
        email: this.email,
        password: this.password,
      });
    },
  },
};
</script>

<style>
.login-container {
  max-width: 400px;
  color: white;
  margin: auto;
  padding: 20px;
  border: 1px solid #0687ff;
  border-radius: 8px;
  background-color: #2d6b4f31;
}

.input-box {
  margin-bottom: 15px;
}

.input-box input {
  width: 95%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.button input {
  background-color: #007bff;
  color: white;
  cursor: pointer;
}

.button input:hover {
  background-color: #0056b3;
}

.error {
  color: red;
  margin-top: 10px;
}

.success {
  color: green;
  margin-top: 10px;
}

.register-link {
  margin-top: 15px;
  text-decoration: none;
  color: rgb(20, 140, 78);
}
</style>
