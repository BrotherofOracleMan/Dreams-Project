<template>
    <div>
        <div class="display-card">
            <div class="close-button" @click="closeCard">X</div>

        <div>
            <label for="dreamName">Dream name</label>
            <p>{{}}</p>
        </div>

        <div>
            <label for="dreamDate">Date:</label>
            <p>{{}}</p>
        </div>

        <div>
            <label for="dreamDescription">Description:</label>
            <p>{{}}</p>
        </div>
        </div>
    </div>
</template>

<script>
export default{
    data(){
        return{
            CardData:{
                Name:'',
                Date:'',
                Description:'',
            }
        }
    },methods:{
        openCard(){
            this.isCardOpen = true
        },
        closeCard(){
            this.isCardOpen= false
        }
    }
}
</script>

<style scoped>
.display-card {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  padding: 20px;
  background-color: #fff;
  border: 1px solid #ccc;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  z-index: 999; /* Adjust z-index as needed */
}

.close-button {
  position: absolute;
  top: 10px;
  right: 10px;
  cursor: pointer;
  font-weight: bold;
  color: #555;
}

button {
  margin-top: 20px;
  padding: 10px;
}

</style>
