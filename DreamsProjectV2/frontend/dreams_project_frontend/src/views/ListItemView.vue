<template>
    <div>
    <h2>List of Dreams</h2>
      <!-- Use v-for to iterate over the items and pass each item to ListViewItem -->
      <ListItem v-for="item in items" :key="item.id" :item="item" class="list-item" />
  </div>
</template>

<script>

import ListItem from '../components/Listitem.vue'

export default{
    components:{
        ListItem,
    },
    props:{
        dreams:0
    },
    data(){
        return {
            items: [
                {id: 1 , name: 'Item 1'},
                {id: 2, name: 'Item 2'},
                {id: 3, name: 'Item 3'}
            ]
        }

    }
}

</script>

<style>

</style>