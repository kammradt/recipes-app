<template>
  <v-app>
    <header>
      <div class="text-box">
        <h1 class="display-3">Receitinhas top 😋</h1>
        <p class="mt-3 font-weight-light headline">
          Recipes for the meals we love ❤️
        </p>
        <v-alert outline :value="failedLogin" type="warning">
          Verify your credencials
        </v-alert>
        <v-form class="pr-5  pt-3">
          <v-text-field
            v-model="loginData.username"
            prepend-icon="person"
            label="Login"
            type="text"
            dark
          />
          <v-text-field
            v-model="loginData.password"
            prepend-icon="lock"
            label="Password"
            type="password"
            dark
          />
        </v-form>

        <v-btn outline color="white" @click="onLogin">
          login
          <v-icon right dark>person</v-icon>
        </v-btn>
      </div>
    </header>
  </v-app>
</template>
<script>
export default {
  head() {
    return {
      title: 'Home page'
    }
  },
  data() {
    return {
      loginData: {
        username: '',
        password: ''
      },
      failedLogin: false
    }
  },
  methods: {
    async onLogin() {
      const headers = { 'Content-Type': 'application/json' }
      try {
        // eslint-disable-next-line no-unused-vars
        const response = await this.$axios.$post(
          '/login/',
          this.loginData,
          headers
        )
        this.$store.dispatch('updateToken', response.token)
        this.$router.push('/recipes/')
      } catch (e) {
        this.failedLogin = true
      }
    }
  }
}
</script>
<style>
header {
  min-height: 100vh;
  background-image: linear-gradient(
      to right,
      rgba(0, 0, 0, 0.9),
      rgba(0, 0, 0, 0.1)
    ),
    url('/images/banner.jpg');
  background-position: center;
  background-size: cover;
  position: relative;
}
.text-box {
  position: absolute;
  top: 50%;
  left: 10%;
  transform: translateY(-50%);
  color: #fff;
}
a {
  text-decoration: none;
}
</style>
