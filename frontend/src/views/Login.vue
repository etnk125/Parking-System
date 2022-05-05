<template>
  <main>
    <form @submit.prevent="login">
      <div class="mb-3">
        <label for="exampleInputEmail1" class="form-label">Email address</label>
        <input type="email" class="form-control" aria-describedby="emailHelp" v-model="form.email" />
      </div>
      <div class="mb-3">
        <label for="exampleInputPassword1" class="form-label">Password</label>
        <input
          type="password"
          class="form-control"
          id="exampleInputPassword1"
          v-model="form.password"
        />
      </div>

      <button type="submit" class="btn btn-primary">Login</button>
    </form>
  </main>
</template>

<script>
import { login } from "../services";
export default {
  data: () => ({
    form: {
      email: "earth@mail.com",
      password: "1234",
    },
  }),
  methods: {
    login() {
      login(this.form)
        .then(({ data }) => {
          console.log(data);
          if (data) {
            this.$router.push("/main/" + data.token);
          }
        })
        .catch((err) => console.log);
    },
  },
};
</script>

<style scoped>
form {
  margin: auto;
  width: 300px;
}
</style>