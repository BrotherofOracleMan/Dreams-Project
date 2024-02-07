<template>
  <div class="search-container">
    <div class="search-bar-container">
      <input type="text" v-model="searchQuery" class="search-bar" placeholder="Search...">
    </div>
    <div class="button-container">
      <button id="search" @click="search">Search</button>
      <button id ="add_dream" @click="addDream">Add Dream</button>
    </div>
  </div>
</template>

<style scoped>
.search-container {
  display: flex;
  justify-content: space-between; /* Distribute items evenly along the main axis */
  align-items: center;
  padding: 0 20px; /* Optional: Add padding to the sides */
  margin-top: 30px;
}

.search-bar-container {
  flex-grow: 1; /* Allow the search bar to grow and take available space */
}

.search-bar {
  width: 100%;
  height: 40px;
  padding: 10px;
  font-size: 16px;
  border: 1px solid #bbb;
  border-radius: 5px;
}

.button-container {
  margin-left: 10px;
  padding: 10px;
  
}

button {
  margin-left: 5px;
  height: 40px;
  background-color: transparent;
}

#add_dream{
  background: #21d57e;
  border: 1px solid#21d57e;
  border-radius: 6px;
  box-shadow: rgba(0, 0, 0, 0.1) 1px 2px 4px;
  box-sizing: border-box;
  color: #FFFFFF;
  cursor: pointer;
  display: inline-block;
  font-family: nunito,roboto,proxima-nova,"proxima nova",sans-serif;
  font-size: 16px;
  font-weight: 800;
  line-height: 16px;
  min-height: 40px;
  outline: 0;
  padding: 12px 14px;
  text-align: center;
  text-rendering: geometricprecision;
  text-transform: none;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  vertical-align: middle;
}

#add_dream:hover,
#add_dream:active {
  background-color: initial;
  background-position: 0 0;
  color: #21d57e;
}

#add_dream:active {
  opacity: .5;
}

#search{
  background: #0b2598;
  border: 1px solid#0b2598;
  border-radius: 6px;
  box-shadow: rgba(0, 0, 0, 0.1) 1px 2px 4px;
  box-sizing: border-box;
  color: #FFFFFF;
  cursor: pointer;
  display: inline-block;
  font-family: nunito,roboto,proxima-nova,"proxima nova",sans-serif;
  font-size: 16px;
  font-weight: 800;
  line-height: 16px;
  min-height: 40px;
  outline: 0;
  padding: 12px 14px;
  text-align: center;
  text-rendering: geometricprecision;
  text-transform: none;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  vertical-align: middle;
}

#search:hover,
#search:active {
  background-color: initial;
  background-position: 0 0;
  color: #0b2598;
}

#search:active {
  opacity: .5;
}

</style>

<script>
export default {
  data() {
    return {
      searchQuery: '',
    };
  },
  methods: {
    search() {
      this.$emit("SearchBarSearch", this.searchQuery)
    },
    extraAction() {
      // Handle extra action logic
     
    },
  },
};
</script>