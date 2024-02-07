<template>
    <div class="search-bar">
        <input type="text" v-model="searchQuery" placeholder="Search ...." />
    </div>
</template>

<script>
//add a search bar and drop down display here
export default {
    data(){
        return {
            searchQuery: '',
        }
    }
}
</script>

<style>

</style>