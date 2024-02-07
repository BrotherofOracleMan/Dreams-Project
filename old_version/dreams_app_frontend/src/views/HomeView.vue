<template>
    <head>
        <title>Dreams Application</title>
    </head>
    <body>
        <h1 id="DreamTitle"> List of Dreams </h1>
        <search-bar/>
    </body>
</template>

<script>
import SingleDream from '@/components/SingleDream.vue'
import SearchBar from '@/components/SearchBar.vue'

export default {
    name: 'Home',
    components: {SearchBar},
    data(){
        return{
            dreams: [],
        }
    },
    mounted(){

    }
}
</script>

<style>

</style>