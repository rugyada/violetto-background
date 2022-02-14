# Violetto theme background
%define oname Violetto
%define bdate   2022.02.14

Summary:	Violetto theme background
Name:		violetto-background
Version:	1
Release:	1
License:	GPL
Group:		Graphics
Url:		https://github.com/rugyada/violetto-background
Source0:	%{oname}.tar.gz

BuildArch:	noarch

%description
Violetto theme background

%files
/usr/share/wallpapers/Violetto

%prep
%setup -qn %{oname}-%{version}

%build


%install
mkdir -p %{buildroot}/usr/share/wallpapers/Violetto
cp -rf * %{buildroot}/usr/share/wallpapers/Violetto/
