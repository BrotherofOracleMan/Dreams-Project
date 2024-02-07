<template>  
    <div>
      <SearchBar />
      <ListItemView />
    </div>
</template>
  
  <script>
  import ListItemView from '../views/ListItemView.vue';
  import SearchBar from '../components/SearchBar.vue';
  export default {
    name: 'HomeView',
    components:{
      ListItemView,
      SearchBar,
    }
  };
  </script>