## users

**GET**: `/api/v1/users`
- Retrieves a list of all users.

**GET**: `/api/v1/users/{id}`
- Retrieves a user identified by the provided {id}.

## cities

**GET** `/api/v1/cities`
- Retrieves a list of all cities.

| q `str, opt` | Filters the cities by name prefix. If provided, the API will return cities whose names start with the specified prefix. |
| ------------ | ----------------------------------------------------------------------------------------------------------------------- |
**GET** `/api/v1/cities/{id}`
- Retrieves a city identified by the provided {id}.

## locations

**GET** `/api/v1/locations`
- Retrieves a list of all locations.
**GET** `/api/v1/locations/{id}`
- Retrieves a location identified by the provided {id}.
**GET** `/api/v1/cities/{id}/locations`
- Retrieves a list of locations within a specific city identified by the provided {id}.
## images

**GET** `/api/v1/images`
- Retrieves a list of all images.
**GET** `/api/v1/images/{id}`
- Retrieves an image identified by the provided {id}.
**GET**  `/api/v1/items/{id}/images`
- Retrieves a list of images of a specific item identified by the provided {id}.
**GET** `/api/v1/vehicles/{id}/images`
- Retrieves a list of images of a specific vehicle identified by the provided {id}.