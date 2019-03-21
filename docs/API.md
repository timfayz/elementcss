# elementcss API

All source code has well-written embedded documentation with several examples per each `@function()` or `@mixin()` definition. Files are logically separated and organized so that you can read them as API sections. That's why the listings below is given as automatically generated set of direct links to the sources.

Files starting with `_css-*` basically means they *also* have `@mixin`(s) that generate CSS code. Otherwise, they only contain function definitions.

### Grid `src/_css-grid.scss`

- [`calc-grid($return, $data)`](https://github.com/timfayz/elementcss/blob/master/src/_css-grid.scss#L18)
- [`grid($type, $data, $query-map:null, $rows:gutter columned, $dir:ltr)`](https://github.com/timfayz/elementcss/blob/master/src/_css-grid.scss#L201)

### SEM utils `src/_css-sem.scss`

- [`add($storage, $p-name, $s-base, $set-data)`](https://github.com/timfayz/elementcss/blob/master/src/_css-sem.scss#L167)
- [`pass-sets($args...)`](https://github.com/timfayz/elementcss/blob/master/src/_css-sem.scss#L182)
- [`sets($storage, $query-map:())`](https://github.com/timfayz/elementcss/blob/master/src/_css-sem.scss#L189)
- [`set($s-base, $p-name, $set-data, $q-map:null)`](https://github.com/timfayz/elementcss/blob/master/src/_css-sem.scss#L280)
- [`pass-set($s-base, $data, $q-map:null)`](https://github.com/timfayz/elementcss/blob/master/src/_css-sem.scss#L287)

### CSS unit utils `src/_unit.scss`

- [`trim-unit($val)`](https://github.com/timfayz/elementcss/blob/master/src/_unit.scss#L53)
- [`append-unit($val, $unit)`](https://github.com/timfayz/elementcss/blob/master/src/_unit.scss#L63)
- [`convert-len($val, $unit, $ref: $convert-len-ref, $ppi: $convert-len-ppi)`](https://github.com/timfayz/elementcss/blob/master/src/_unit.scss#L94)
- [`round-len($val, $unit:detect, $ref: $convert-len-ref, $ppi:$convert-len-ppi)`](https://github.com/timfayz/elementcss/blob/master/src/_unit.scss#L155)
- [`adopt-len($val, $parent: $adopt-len-parent, $base: $adopt-len-base)`](https://github.com/timfayz/elementcss/blob/master/src/_unit.scss#L236)
- [`convert-angle($val, $unit:'', $round: true)`](https://github.com/timfayz/elementcss/blob/master/src/_unit.scss#L260)
- [`convert-time($val, $unit:null)`](https://github.com/timfayz/elementcss/blob/master/src/_unit.scss#L303)

### Miscellaneous `src/_css-utils.scss`

- [`clearfix()`](https://github.com/timfayz/elementcss/blob/master/src/_css-utils.scss#L6)
- [`font-face($font-family, $font-path, $formats:null, $font-weight:normal, $font-style:normal, $svg-font-name:null, $version:null)`](https://github.com/timfayz/elementcss/blob/master/src/_css-utils.scss#L25)
- [`media($key, $map:null)`](https://github.com/timfayz/elementcss/blob/master/src/_css-utils.scss#L79)
- [`container($data, $query-map:())`](https://github.com/timfayz/elementcss/blob/master/src/_css-utils.scss#L144)
- [`ruler($line-height: 16px, $color: rgba(0,0,0,0.2), $z-index: null, $type: horizontal)`](https://github.com/timfayz/elementcss/blob/master/src/_css-utils.scss#L219)
- [`icon-set($font-family:null, $class-prefix:null, $pseudo-element:before, $content-map:(), $from-title:false)`](https://github.com/timfayz/elementcss/blob/master/src/_css-utils.scss#L260)

### Color utils `src/_color.scss`

- [`shade($clr, $percentage)`](https://github.com/timfayz/elementcss/blob/master/src/_color.scss#L10)
- [`tint($clr, $percentage)`](https://github.com/timfayz/elementcss/blob/master/src/_color.scss#L21)
- [`brightness($clr, $algorithm:$brightness-algorithm)`](https://github.com/timfayz/elementcss/blob/master/src/_color.scss#L78)
- [`contrast-color($clr, $dark, $light, $algorithm:$brightness-algorithm)`](https://github.com/timfayz/elementcss/blob/master/src/_color.scss#L92)
- [`contrast-ratio($c1, $c2, $algorithm:$brightness-algorithm)`](https://github.com/timfayz/elementcss/blob/master/src/_color.scss#L107)
- [`hsl($hue, $sat, $light, $alpha:1)`](https://github.com/timfayz/elementcss/blob/master/src/_color.scss#L171)
- [`hwb($hue, $white, $black, $alpha:1)`](https://github.com/timfayz/elementcss/blob/master/src/_color.scss#L205)
- [`hsv($hue, $sat, $value, $alpha:1)`](https://github.com/timfayz/elementcss/blob/master/src/_color.scss#L241)
- [`device-cmyk($cyan, $magneta, $yellow, $key, $alpha:1)`](https://github.com/timfayz/elementcss/blob/master/src/_color.scss#L275)
- [`gray($v, $alpha:1)`](https://github.com/timfayz/elementcss/blob/master/src/_color.scss#L292)
- [`render-color($clr, $model)`](https://github.com/timfayz/elementcss/blob/master/src/_color.scss#L306)
- [`color($args)`](https://github.com/timfayz/elementcss/blob/master/src/_color.scss#L401)

### String utils `src/_string.scss`

- [`prefix($val, $prefix:'-', $onNull:false, $except:root)`](https://github.com/timfayz/elementcss/blob/master/src/_string.scss#L10)
- [`postfix($val, $postfix:'-', $onNull:false, $except:root)`](https://github.com/timfayz/elementcss/blob/master/src/_string.scss#L22)
- [`get-number($str, $unit:true, $sign:true, $start:1)`](https://github.com/timfayz/elementcss/blob/master/src/_string.scss#L135)
- [`get-numbers($str, $unit:true, $sign:true, $start:1, $max:null)`](https://github.com/timfayz/elementcss/blob/master/src/_string.scss#L149)
- [`str-exists($str, $substr)`](https://github.com/timfayz/elementcss/blob/master/src/_string.scss#L169)
- [`has-prefix($str, $prefix)`](https://github.com/timfayz/elementcss/blob/master/src/_string.scss#L182)
- [`has-postfix($str, $postfix)`](https://github.com/timfayz/elementcss/blob/master/src/_string.scss#L200)
- [`str-replace($str, $old, $new, $n:1)`](https://github.com/timfayz/elementcss/blob/master/src/_string.scss#L261)
- [`trim-left($str, $cutset)`](https://github.com/timfayz/elementcss/blob/master/src/_string.scss#L289)
- [`trim-right($str, $cutset)`](https://github.com/timfayz/elementcss/blob/master/src/_string.scss#L312)

### Lists utils `src/_list.scss`

- [`wrap($list)`](https://github.com/timfayz/elementcss/blob/master/src/_list.scss#L10)
- [`unwrap($list)`](https://github.com/timfayz/elementcss/blob/master/src/_list.scss#L20)
- [`n($list, $indexes...)`](https://github.com/timfayz/elementcss/blob/master/src/_list.scss#L35)
- [`nth-retrieve($list, $indexes, $separator:auto)`](https://github.com/timfayz/elementcss/blob/master/src/_list.scss#L69)
- [`nth-remove($list, $indexes, $separator:auto)`](https://github.com/timfayz/elementcss/blob/master/src/_list.scss#L146)
- [`nth-set($list, $indexes, $val:null, $separator:auto)`](https://github.com/timfayz/elementcss/blob/master/src/_list.scss#L166)
- [`nth-replace($list, $indexes, $old:null, $new:null, $separator:auto)`](https://github.com/timfayz/elementcss/blob/master/src/_list.scss#L188)
- [`nth-insert($list, $indexes, $val:null, $mode:post wrap, $separator:auto)`](https://github.com/timfayz/elementcss/blob/master/src/_list.scss#L219)
- [`indexes($list1, $list2, $type:inter, $abs:false)`](https://github.com/timfayz/elementcss/blob/master/src/_list.scss#L243)
- [`inter($list1, $list2, $abs:false, $separator:auto)`](https://github.com/timfayz/elementcss/blob/master/src/_list.scss#L297)
- [`diff($list1, $list2, $abs:false, $separator:auto)`](https://github.com/timfayz/elementcss/blob/master/src/_list.scss#L315)
- [`union($list1, $list2, $mode:post, $abs:false, $separator:auto)`](https://github.com/timfayz/elementcss/blob/master/src/_list.scss#L337)
- [`slice($list, $start:1, $end:length($list), $separator:auto)`](https://github.com/timfayz/elementcss/blob/master/src/_list.scss#L362)
- [`collate($args...)`](https://github.com/timfayz/elementcss/blob/master/src/_list.scss#L398)
- [`replace($list, $old, $new:null, $mode:all, $separator:auto)`](https://github.com/timfayz/elementcss/blob/master/src/_list.scss#L514)
- [`remove($list, $vals, $separator:auto)`](https://github.com/timfayz/elementcss/blob/master/src/_list.scss#L582)
- [`list-map($list)`](https://github.com/timfayz/elementcss/blob/master/src/_list.scss#L596)
- [`before($list, $val)`](https://github.com/timfayz/elementcss/blob/master/src/_list.scss#L616)
- [`after($list, $val)`](https://github.com/timfayz/elementcss/blob/master/src/_list.scss#L635)

### Map utils `src/_map.scss`

- [`m($map, $keys...)`](https://github.com/timfayz/elementcss/blob/master/src/_map.scss#L13)
- [`nth-key($map, $n)`](https://github.com/timfayz/elementcss/blob/master/src/_map.scss#L28)
- [`nth-value($map, $n)`](https://github.com/timfayz/elementcss/blob/master/src/_map.scss#L36)
- [`map-empty($m, $mode:false)`](https://github.com/timfayz/elementcss/blob/master/src/_map.scss#L49)
- [`map-replace($map1, $map2)`](https://github.com/timfayz/elementcss/blob/master/src/_map.scss#L69)
- [`map-union($map1, $map2, $mode:post, $separator:auto)`](https://github.com/timfayz/elementcss/blob/master/src/_map.scss#L86)
- [`map-list($map, $separator:auto)`](https://github.com/timfayz/elementcss/blob/master/src/_map.scss#L110)
- [`map-get-key($map, $val)`](https://github.com/timfayz/elementcss/blob/master/src/_map.scss#L123)

### Math `src/_math.scss`

- [`gcd($a, $b)`](https://github.com/timfayz/elementcss/blob/master/src/_math.scss#L10)
- [`pow($base, $exp, $prec: 12)`](https://github.com/timfayz/elementcss/blob/master/src/_math.scss#L24)
- [`root($num, $n: 2, $prec: 12)`](https://github.com/timfayz/elementcss/blob/master/src/_math.scss#L52)
- [`limit($val, $min, $max)`](https://github.com/timfayz/elementcss/blob/master/src/_math.scss#L64)
- [`scale($val, $amount, $min:0, $max:100)`](https://github.com/timfayz/elementcss/blob/master/src/_math.scss#L76)
- [`max($args...)`](https://github.com/timfayz/elementcss/blob/master/src/_math.scss#L93)
- [`min($args...)`](https://github.com/timfayz/elementcss/blob/master/src/_math.scss#L103)

### Found broken links?
Please, [open](https://github.com/timfayz/elementcss/issues) an issue or [write](mailto:timfayz.only@gmail.com?subject=elementcss.%20Issue) me an email. 