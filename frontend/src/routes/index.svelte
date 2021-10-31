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
                       <div class="overflow-x-auto">
                         <table class="table w-full table-compact">
                           <thead>
                             <tr>
                               <th>Name</th>
                               <th>Price</th>
                               <th>Amount</th>
                               <th>Regularity</th>
                               <th>Purchase?</th>
                             </tr>
                           </thead>
                           <tbody>
                               {#each phones as phone, i}
                                   <tr>
                                       <td>
                                         {phone.name}
                                       </td>
                                       <td>
                                         {phone.price*phone.amount}
                                       </td>
                                       <td>
                                          <select class="select" bind:value={phone.amount}>
                                            <option disabled>Amount</option>
                                            {#each Array(10) as _, i}
                                              <option>{i+1}</option>
                                            {/each}
                                          </select>
                                       </td>
                                       <td>
                                         {phone.regularity}
                                       </td>
                                       <td>
                                          <div class="form-control">
                                            <label class="cursor-pointer label">
                                              <input type="checkbox" checked={false} class="checkbox checkbox-primary"
                                                value={phone} bind:group={selectedPhones}>
                                            </label>
                                        </div>
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
	</main>
	<Footer />
</body>
