
![](https://i.imgur.com/i7LhlTB.png)
## static_cast

The `static_cast` reverses a well-defined implicit conversion.

```cpp
short increment_as_short(void*u target) { 
	short as_short = static_cast(target); 
	*as_short = *as_short + 1; 
	return *as_short; 
}
```

## reinterpret_cast

The `reinterpret_cast` gives control when type conversions that are not well defined needed.

```cpp
#include <cstdio>

int main() {
 auto timer = reinterpret_castu<const unsigned long*>(0x1000);
 printf("Timer is %lu.", *timer);
}
int main() {
	const unsigned long* timer{ 0x1000 }; // this will not work.
}
```