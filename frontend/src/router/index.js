import { createRouter, createWebHistory } from "vue-router";
// import page
import Login from "../views/Login.vue";
import Main from "../views/Main.vue";
import Register from "../views/Register.vue";

// using web history
const routerHistory = createWebHistory();

// routing
// https://router.vuejs.org/guide/migration/#removed-star-or-catch-all-routes
const routes = [
  { path: "/", redirect: "/login" },
  { path: "/login", name: "Login", component: Login },
  { path: "/main/:token", name: "Main", component: Main, props: true },
  { path: "/register", name: "Register", component: Register },
  { path: "/:pathMatch(.*)*", redirect: "/" },
];

// create router
const router = createRouter({
  history: routerHistory,
  routes,
});

// export router
export default router;
