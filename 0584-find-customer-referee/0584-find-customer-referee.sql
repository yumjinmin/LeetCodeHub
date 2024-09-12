SELECT name FROM Customer WHERE referee_id != 2 or referee_id is null;

# null값은 자동으로 제외되기 때문에 COALESCE(column, replace_value)로 null을 0으로 바꾸어 준 다음 조건을 걸어주면 된다.
SELECT name FROM Customer WHERE COALESCE(referee_id, 0) != 2;
