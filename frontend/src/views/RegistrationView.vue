<template>
  <div class="registration-container">
    <h2>Регистрация</h2>
    <form @submit.prevent="registerUser">
      <div class="input-box">
        <input
          type="text"
          v-model="name"
          placeholder="Введите ваше имя"
          required
        />
      </div>
      <div class="input-box">
        <input
          type="email"
          v-model="email"
          placeholder="Введите вашу почту"
          required
        />
      </div>
      <div class="input-box">
        <input
          type="password"
          v-model="password"
          placeholder="Придумайте пароль"
          required
        />
      </div>
      <div class="input-box">
        <input
          type="password"
          v-model="confirmPassword"
          placeholder="Подтвердите пароль"
          required
        />
      </div>
      <div class="policy">
        <input type="checkbox" v-model="acceptTerms" required />
        <label>Я принимаю правила и условия пользования</label>
      </div>
      <div class="input-box button">
        <input type="submit" value="Зарегестрироваться" />
      </div>
      <div v-if="error" class="error">{{ error }}</div>
      <div v-if="success" class="success">{{ success }}</div>
    </form>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";

export default {
  data() {
    return {
      name: "",
      email: "",
      password: "",
      confirmPassword: "",
      acceptTerms: false,
    };
  },
  computed: {
    ...mapState("auth", ["error", "success", "isLoggedIn"]),
  },
  methods: {
    ...mapActions("auth", ["register"]),
    registerUser() {
      if (this.password !== this.confirmPassword) {
        this.$store.commit("auth/SET_ERROR", "Passwords do not match");
        return;
      }

      this.register({
        email: this.email,
        password: this.password,
      });
    },
  },
};
</script>

<style>
.registration-container {
  color: white;
  max-width: 400px;
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
  width: 100%;
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
</style>
