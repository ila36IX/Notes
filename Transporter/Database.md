- **Users**
    - id (Primary Key)
    - created_at
    - updated_at
    - password
    - email
    - first_name
    - last_name
    - phone
    - birthday
    - img_id
- cities
	- id
	- name
	
- Locations
	- id
	- name
	- city_id

- **Drivers**    
    - user_id (Primary Key, Foreign Key)
    - license_number
    - vehicle_id
    - current_location_id
    - availability_status (Enroute, Inactive, Available)

- **Customers**
	- id
    - user_id (Primary Key, Foreign Key)
    - company (optional)

- **Items**
    - id (Primary Key)
    - customer_id (Foreign Key)
    - description
    - weight
    - size_x
    - size_y
    - pickup_location_id
    - delivery_location_id
    

- Vehicles
	- id
	- model
	- year
	- capacity

- vehcle_images
	- id
	- vehicle_id
	- image_id

- item_images
	- id
	- item_id
	- image_id

- images
	- id
	- img_path
	- img_url

- **Deliveries**
    - id (Primary Key)
    - item_id (Foreign Key)
    - driver_id (Foreign Key)
    - Pickup_time
    - delivery_time
    - status (Pending, In Transit, Delivered)
    
- **Ratings**
    - id (Primary Key)
    - rated_driver_id (Foreign Key)
    - rater_customer_id (Foreign Key)
    - rating (max 5)
    - comment (string)
# Claude advices

The database design looks good overall, but I would suggest a few changes:

1. **Users Table**:
   - The `img_id` column should be nullable since not all users may have an associated image.
   - Instead of having a `cities` column, it would be better to have a separate `user_cities` table to represent the many-to-many relationship between users and cities.

2. **Drivers Table**:
   - The `user_id` column should be a foreign key referencing the `Users` table, not a primary key.
   - The `current_location_id` column should be nullable since a driver may not have a current location when they are not active.

3. **Customers Table**:
   - The `user_id` column should be a primary key, not the `id` column. This way, you can avoid duplicating user information in both the `Users` and `Customers` tables.

4. **Items Table**:
   - Add a `status` column to track the item's status (e.g., "Pending Pickup", "In Transit", "Delivered").

5. **Vehicles Table**:
   - Add a `driver_id` column to associate a vehicle with a driver.

6. **Deliveries Table**:
   - Add a `pickup_location_id` and `delivery_location_id` column to store the pickup and delivery locations for each delivery.
   - The `status` column could be an enum type with values like "Pending", "In Transit", "Delivered", etc.

7. **Ratings Table**:
   - Add a `delivery_id` column to associate the rating with a specific delivery.

8. **Additional Tables**:
   - Create a `user_locations` table to represent the many-to-many relationship between users and locations.
   - Create a `vehicle_types` table to store different vehicle types (e.g., sedan, van, truck) and associate each vehicle with a type.

9. **Relationships**:
   - Define the appropriate relationships between tables (one-to-one, one-to-many, many-to-many) using foreign keys and association tables where necessary.

10. **Indexes**:
    - Add appropriate indexes on columns that will be frequently used in queries, such as `user_id`, `driver_id`, `item_id`, `location_id`, etc., to improve query performance.

11. **Data Integrity**:
    - Ensure data integrity by adding constraints (e.g., unique constraints, check constraints) where appropriate.

12. **Naming Conventions**:
    - Follow a consistent naming convention for tables and columns (e.g., snake_case or PascalCase).

Overall, the database design looks reasonable, but these changes should help improve data integrity, performance, and maintainability.
