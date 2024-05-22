<template>
  <div class="password-reset">
    <h2>Восстановление пароля</h2>
    <form @submit.prevent="sendResetCode" v-if="!resetCodeSent">
      <label for="email">Ввести почту:</label>
      <input type="email" id="email" v-model="email" required />
      <button type="submit">Отправить код восстановления</button>
    </form>
    <form @submit.prevent="resetPassword" v-if="resetCodeSent">
      <label for="resetCode">Ввести код:</label>
      <input type="text" id="resetCode" v-model="resetCode" required />
      <label for="newPassword">Ввести пароль:</label>
      <input type="password" id="newPassword" v-model="newPassword" required />
      <button type="submit">Воссатновить пароль</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      email: "",
      resetCode: "",
      newPassword: "",
      resetCodeSent: false,
    };
  },
  methods: {
    sendResetCode() {
      console.log("Reset code sent to email:", this.email);
      this.resetCodeSent = true;
    },
    resetPassword() {
      console.log(
        "Resetting password with code:",
        this.resetCode,
        "and new password:",
        this.newPassword
      );
    },
  },
};
</script>

<style scoped>
.password-reset {
  max-width: 400px;
  margin: 0 auto;
}

.password-reset form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.password-reset label {
  font-weight: bold;
}

.password-reset input {
  padding: 0.5rem;
  font-size: 1rem;
}

.password-reset button {
  padding: 0.5rem;
  font-size: 1rem;
  background-color: #007bff;
  color: white;
  border: none;
  cursor: pointer;
}

.password-reset button:hover {
  background-color: #0056b3;
}
</style>
