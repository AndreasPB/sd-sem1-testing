<script>
	import Footer from '../components/footer.svelte';
	import Navbar from '../components/navbar.svelte';

    const addPhone = (phone) => {
        selectedPhones = [...selectedPhones, phone];
    }

    const removePhone = (index) => {
        selectedPhones.splice(index, 1);
        selectedPhones = selectedPhones;
    }

    let phoneLines = 0;
    let selectedPhone;
    let selectedPhones = [];
    let phones = [
        {
            "name": "Motorola G99",
            "price": 800,
            "amount": 4,
            "regularity": "Once",
        },
        {"name": "iPhone 99", "price": 6000, "amount": 1, "regularity": "Once"},
    ];
</script>

<body class="flex flex-col h-screen justify-between">
	<Navbar />
	<main class="flex-grow">
		<div class="container mx-auto">
            <!-- Main phone card -->
            <div class="mt-5 card bordered">
                <div class="card-body">
                    <h2 class="card-title">KEANet</h2>
                    <!-- Internet connection -->
                    <div class="p-6 card bordered">
                        <div class="form-control">
                            <label class="cursor-pointer label">
                                <span class="label-text">Internet connection</span>
                                <input type="checkbox" checked={false} class="checkbox checkbox-primary">
                            </label>
                        </div>
                    </div>
                    <!-- Phone line -->
                    <p>Phone lines: {phoneLines}</p>
                    <input type="range" max="8" bind:value={phoneLines} class="range range-primary">
                    <!-- Cell phones -->
                    <p>Cell phones:</p>
                    <div class="flex flex-col w-full lg:flex-row">
                       <select class="select select-bordered w-full max-w-xs" bind:value={selectedPhone}>
                          <option disabled>Select phones</option>
                          {#each phones as phone}
                              <option value={phone}>{phone.name}</option>
                          {/each}
                       </select>
                       <div class="divider divider-vertical">
                           <button class="btn-ghost" on:click={addPhone(selectedPhone)}>&gt</button>
                           <button class="btn-ghost" on:click={removePhone(selectedPhones[selectedPhones.length - 1])}> &lt </button>
                       </div>
                       <div class="overflow-x-auto">
                         <table class="table w-full table-compact">
                           <thead>
                             <tr>
                               <th></th>
                               <th>Name</th>
                               <th>Price</th>
                               <th>Amount</th>
                               <th>Regularity</th>
                             </tr>
                           </thead>
                           <tbody>
                               {#each selectedPhones as phone, i}
                                   <tr>
                                       <th>
                                           {i + 1}
                                       </th>
                                       <td>
                                         {phone.name}
                                       </td>
                                       <td>
                                         {phone.price}
                                       </td>
                                       <td>
                                         {phone.amount}
                                       </td>
                                       <td>
                                         {phone.regularity}
                                       </td>
                                   </tr>
                               {/each}
                           </tbody>
                         </table>
                       </div>
                    </div>
                    <!-- Total price -->
                    <h2>Total price: 0 DKK</h2>
                    <!-- Buy button -->
                    <button class="btn btn-primary">Buy</button>
                </div>
            </div>
		</div>
	</main>
	<Footer />
</body>
