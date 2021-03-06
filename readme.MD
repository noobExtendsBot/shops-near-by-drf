# This Project implements REST API for the [article](https://realpython.com/location-based-app-with-geodjango-tutorial/#creating-a-django-application).

---

## INFO:

> Project layout is different from the artice mentioned, but `nearbyshops` goes under `geoapp` and `api` folder has all the DRF parts.
> There are two views `GetAllShops` and `GetNearByShops`. First one returns all the shops from DB, second one takes: `longitude` and `latitude` in URL. Like:`http://127.0.0.1:8000/geo/app/shops/near/me/?longitude=30.3340&latitude=77.9602`

---

## usage

1. Check `requirements.txt`, need to install two extra packages `django-extra-fields==2.0.5`
   `djangorestframework==3.11.0`

API output:

1. [GetAllShops](http://127.0.0.1:8000/geo/app/all/shops/)

![output](./output_results/all_shops.png)

2. [GetNearByShops](http://127.0.0.1:8000/geo/app/shops/near/me/?longitude=30.3340&latitude=77.9602)

![output](./output_results/shops_near_me.png)
