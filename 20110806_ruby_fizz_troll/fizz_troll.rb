def fizz_buzz number
  text = ""
  text += "fizz" if number % 3 == 0
  text += "buzz" if number % 5 == 0
  return text unless text.empty?
  number 
end

class Fixnum
  def divided_by number
    self % number == 0
  end
end

def fizz_intro number
  if number.divided_by 15
    "fizzbuzz"
  elsif number.divided_by 3
    "fizz"
  elsif number.divided_by 5
    "buzz"
  else
    number
  end
end

class Fixnum
  def fizz_in
    fizz_buzz(self)
  end
end

def fizz_tern number
  (number.divided_by 3 ? (number.divided_by 5 ? "fizzbuzz" : "fizz") : (number.divided_by 5 ? "buzz" : number)) 
end


def fizz_map number
  hash = {
    3 => "fizz",
    5 => "buzz"
  }
  text = ""
  hash.keys.sort.each do |key|
    text += hash[key] if number.divided_by key
  end
  text.empty? ? number : text
end

def fizz_select number
  special = Hash.new{ |h, k| h[k] = k }
  special[""] = number

  hash = { 3 => "fizz", 5 => "buzz" }
  special[hash.select{|k,v| number % k==0}.collect{|k| k[1]}.sort.reverse.join("")]  
end  
