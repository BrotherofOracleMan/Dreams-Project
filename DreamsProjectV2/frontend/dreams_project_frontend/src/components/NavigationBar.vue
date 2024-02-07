<template>
    <nav class="navbar">
    <div class="navbar-content">
      <div class="navbar-title">
        <router-link class="no-underline" to="/">Dreams Application</router-link>
      </div>
      <ul class="navbar-links">
      </ul>
    </div>
  </nav>
</template>

<style scoped>
.navbar {
  background-color: rgb(19, 92, 141);
  color: rgb(233, 224, 224);
  padding: 10px;
  text-decoration: none;

}

.navbar-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.navbar-title {
  text-decoration: none;
  font-size: 1.5rem;
  pointer-events: none;

}

ul {
  list-style-type: none;
  padding: 0;
  display: flex;
}

a{
    color: aliceblue;
    text-decoration: none;
}


</style>