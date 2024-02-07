<template>
    <div id="app">
    <NavigationBar />
    <p class="description">This is a Dreams Application. Search or add Dreams according to your liking. </p>
    <router-view></router-view>
  </div>
</template>

<script>
import NavigationBar from '@/components/NavigationBar.vue';

export default {
  name: 'App',
  components: {
    NavigationBar
  },
  created(){
    console.log("Created lifecycle hook for App.vue")
  }
}
</script>

<style scoped>
#app {
  font-family: Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
.description{
  font-size: large;
  padding-top: 40px;
  
}
</style>
